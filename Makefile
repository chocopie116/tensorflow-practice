setup:
	#pyenv install 3.5.2
	#pyenv rehash
	#pyenv virtualenv 3.5.2 TensorFlow
	#pyenv rehash
	#pyenv global TensorFlow
	#python -V
	#pip install --upgrade https://storage.googleapis.com/tensorflow/mac/tensorflow-0.9.0-py3-none-any.whl

#run local server(tensor board app)
tensorboard:
	tensorboard --logdir=./log
