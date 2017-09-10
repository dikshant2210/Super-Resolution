## Super Resolution

Super Resolution is an image enhancement technique to convert low resolution images to high resolution images while maintaining the quality and details of the image.

This repository is an attempt to implement the deep neural architecture proposed in the recent research paper [GUN: Gradual Upsampling Network for single image super-resolution](http://arxiv.org/abs/1703.04244).

Paper discusses about recent advancements made in super resolution and how the approach discussed is different and produces better result compared to previous used architectures. The model proposed differentiates itself from other methods by gradually upsampling the images. Generally, researchers upsample image to desired resolution and then construct the details though in this paper author has highlighted the importance of gradual reconstruction and upsampling.    

### Architecture
![gun.png](https://user-images.githubusercontent.com/10988708/30248664-98f5078e-961b-11e7-9b2b-7a2350c18e43.png)

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```
