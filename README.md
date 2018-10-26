# Neural-Style-transfer
This project is based on Neural style transfer, where we have to generate image such that it has content of content image and style of style image. ![NST.ipynb](https://github.com/Shreeyash-iitr/Neural-Style-transfer/blob/master/NST.ipynb) includes code for NST written in keras. 
Separate loss function according to the formulae given in ![original paper](https://github.com/Shreeyash-iitr/Neural-Style-transfer/blob/master/NST.pdf) (for content loss and style loss) are made in keras. **fmin_l_bfgs_b optimizer** from scipy library is used to minimize net loss function and generate image. Generated image contains the content of content image in style of style image.

## Content Image
<img src="content.jpg" height="400" width="400">

## Style Image
<img src="style.jpg" height="400" width="400">
