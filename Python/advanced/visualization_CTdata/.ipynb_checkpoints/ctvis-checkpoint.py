import numpy as np
import pandas as pd
from glob import glob
import nibabel as nib
import os
import matplotlib.pyplot as plt


# このモジュール内でしか呼ばれないような関数をプライベート関数といい、アンダースコアで明示する
def _get_df(folder='../../sample_data/public_covid_data/rp_im'):
    '''
    絶対パスまたは相対パスを指定して配下のファイルパスとファイル名のDataFrameを返す
    '''
    files = glob(folder+'/*')
    filenames = [os.path.split(file)[1] for file in files]
    return pd.DataFrame({'FilePath':files,'FileName':filenames})


# プライベート関数の説明のために作った。いらない関数。
def get_df_all():
    rp_im_df = _get_df('../../sample_data/public_covid_data/rp_im')
    rp_msk_df = _get_df('../../sample_data/public_covid_data/rp_msk')
    return rp_im_df.merge(rp_msk_df, on='FileName', suffixes=('Image', 'Mask'))


def load_nifti(path):
    '''
    nifti画像データを読み込み、縦横を入れ替えたnumpy arrayを返す
    '''
    return np.rollaxis(nib.load(path).get_fdata(), axis=1, start=0)


def label_color(mask_volume, 
                ggo_color = [255, 0, 0],
                consolidation_color = [0, 255, 0],
                effusion_color = [0, 0, 255]):
    '''
    (縦、横、断面)の3次元マスクデータを読み込み、マスクの値に対応する
    カラーラベルを設定した4次元配列を返す。
    '''
    shp = mask_volume.shape
    # 輝度値のを含んだ4次元ゼロ配列を作成
    mask_color = np.zeros((shp[0], shp[1], shp[2], 3),dtype=np.float32)

    # 色付け。mask_volumeの各要素とラベル番号が等しい箇所へカラーラベルのリストを代入
    mask_color[np.equal(mask_volume, 1)] = ggo_color
    mask_color[np.equal(mask_volume, 2)] = consolidation_color
    mask_color[np.equal(mask_volume, 3)] = effusion_color
    
    return mask_color


def hu_to_gray(volume):
    '''
    CTデータを受け取り、HUを0-255に変換する。
    変換後、マスクデータと同じshapeに揃えた配列を返す。
    '''
    
    maxhu = np.max(volume)
    minhu = np.min(volume)
    # 値を0-255に変換する
    volume_rerange = (volume - minhu) / max((maxhu - minhu), 1e-3)
    volume_rerange = volume_rerange * 255
    
    # マスクと重ねるために、volume_rerangeのshapeを合わせる
    volume_rerange = np.stack([volume_rerange, volume_rerange, volume_rerange], axis=-1)
    
    # 0-255のintにしたいので、下記のようにuint8として返す
    return volume_rerange.astype(np.uint8)


def overlay(gray_volume, mask_volume, mask_color, alpha):
    '''
    グレイスケールのCTデータ、マスクデータ、カラーのマスクデータを受け取り、
    CTデータとマスクデータを重ね合わせた配列を返す。
    '''
    mask_filter = np.greater(mask_volume, 0)
    mask_filter = np.stack([mask_filter, mask_filter, mask_filter], axis=-1)
    overlayed = np.where(mask_filter, 
                         ((1-alpha)*gray_volume + alpha*mask_color).astype(np.uint8),
                         gray_volume)
    
    return overlayed


def vis_overlay(overlayed, original_volume, mask_volume, 
                cols=5, display_num=25, figsize=(15, 15)):
    rows = (display_num - 1) // cols + 1
    total_num = overlayed.shape[-2]
    '''
    CTデータとマスクデータを重ね合わせたプロットを表示する
    '''
    # 表示するスライスの間隔を設定。総スライス数よりも表示枚数が多い場合、1未満になるので、このときは1とする。
    interval = total_num / display_num
    if interval < 1:
        interval = 1
    
    fig, ax = plt.subplots(rows, cols, figsize=figsize)
    # 行列のインデックスはリストのiをカラム数で割った商と余りになる。
    for i in range(display_num):
        row_i = i//cols
        col_i = i%cols
        idx = int(i * interval)
        # idxがtotal_num以上になると、out of indexになるのでbreakする。
        if idx >= total_num:
            break
        # HUの統計量情報を取得 
        # 各スライスごとに統計量を求めたいのでidxを指定して渡す。
        stats = get_hu_stats(original_volume[:, :, idx], 
                               mask_volume[:, :, idx])
        title = 'slice #: {}'.format(idx)
        title += '\nggo mean: {:.0f}±{:.0f}'.format(stats['ggo_mean'],stats['ggo_std'])
        title += '\nconsoli mean: {:.0f}±{:.0f}'.format(stats['consolidation_mean'],stats['consolidation_std'])
        title += '\neffusion mean: {:.0f}±{:.0f}'.format(stats['effusion_mean'],stats['effusion_std'])
        ax[row_i, col_i].imshow(overlayed[:, :, idx])
        # タイトルをつけて軸を消す
        ax[row_i, col_i].set_title(title)
        ax[row_i, col_i].axis('off')
        
    # すっきりさせる
    fig.tight_layout()
        
# volume,mask_volumeは3次元でも2次元（スライス指定）でも動く。
def get_hu_stats(volume, 
                 mask_volume,
                label_dict={1: 'ggo', 2: 'consolidation', 3: 'effusion'}):
    # 統計量格納用辞書を定義
    result = {}

    for label in label_dict.keys():
        # label(key)に対応するvalueがprefix(統計量につける接頭辞)に入る
        prefix = label_dict[label]
        # mask値でvolumeをフィルタリング
        roi_hu = volume[np.equal(mask_volume, label)]
        result[prefix + '_mean'] = np.mean(roi_hu)
        result[prefix + '_std'] = np.std(roi_hu)
        
    return result
