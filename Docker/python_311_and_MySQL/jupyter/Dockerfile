# ベースとなるDockerイメージを指定
FROM python:3.11-slim-bookworm

# 必要なパッケージをインストール
RUN apt-get update && \
	apt-get install -y libgl1-mesa-glx && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* && \
	pip install --upgrade pip && \
	pip install torch torchvision scipy numpy pandas matplotlib seaborn polars scikit-learn thop albumentations opencv-python imgaug torchtext nltk gensim portalocker && \
	rm -rf ~/.cache/pip


# JupyterLab関連のパッケージ
RUN python3 -m pip install --upgrade pip \
&&  pip install --no-cache-dir \
    black \
    jupyterlab \
    jupyterlab_code_formatter \
    jupyterlab-git \
    lckr-jupyterlab-variableinspector \
    jupyterlab_widgets \
    ipywidgets \
    import-ipynb


WORKDIR /
RUN mkdir /work

# execute jupyterlab as a default command
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]