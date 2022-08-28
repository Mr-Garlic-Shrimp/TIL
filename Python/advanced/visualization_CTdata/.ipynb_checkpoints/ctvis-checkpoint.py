import numpy as np
import pandas as pd
from glob import glob
import nibabel as nib
import os


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
    # 輝度値を含んだ4次元配列を作成
    mask_color = np.zeros((shp[0], shp[1], shp[2], 3),dtype=np.float32)

    # 色付け。mask_volumeの各要素とラベル番号が等しい箇所へカラーラベルのリストを代入
    mask_color[np.equal(mask_volume, 1)] = ggo_color
    mask_color[np.equal(mask_volume, 2)] = consolidation_color
    mask_color[np.equal(mask_volume, 3)] = effusion_color
    
    return mask_color