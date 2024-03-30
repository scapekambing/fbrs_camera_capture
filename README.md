## f-BRS with Camera Capture

This fork provides code for deploying the f-BRS demo with an image captured from a camera. In this fork, the ability to load a picture using camera footage is featured. See the original repository to use f-BRS's other features. We have retained all the original source files and added files as per our needs.

## Setting up an environment

This was tested using a Windows 11 machine running Python 3.12 and relies on the PyTorch 1.4.0+. The following command installs all necessary packages:

```.bash
pip install -r requirements.txt
```
to install the Pytorch requirements, follow the **pip** instructions in https://pytorch.org/get-started/locally/


## Interactive Segmentation Demo
1. Be sure to store the pretrained models in a known location. 

2. Run the following:

    ```bash
    # This command runs interactive demo with ResNet-34 model from cfg.INTERACTIVE_MODELS_PATH on GPU with id=0
    # --checkpoint can be relative to cfg.INTERACTIVE_MODELS_PATH or absolute path to the checkpoint
    py demo.py --checkpoint=resnet34_dh128_sbd --gpu=0

    # This command runs interactive demo with ResNet-34 model from the root directory
    # If you also do not have a lot of GPU memory, you can reduce --limit-longest-size (default=800)
    py demo.py --checkpoint=resnet34_dh128_sbd.pth --limit-longest-size=400 --gpu=0

    # You can try the demo in CPU only mode
    py demo.py --checkpoint=resnet34_dh128_sbd --cpu
    ```
3. The camera will launch
4. Press 'q' when desired pose has been made
5. This will load the image onto the f-BRS interactive demo canvas
6. You can now perform the desired f-BRS segmentation! 
7. Hit 'Save mask'

# Pretrained models
The pretrained models with different backbones for interactive segmentation were provided in the original repository. The following is reiterated from the original repository.

The evaluation results are different from the ones presented in our paper, because we have retrained all models on the new codebase presented in this repository. We greatly accelerated the inference of the RGB-BRS algorithm - now it works from 2.5 to 4 times faster on SBD dataset compared to the timings given in the paper. Nevertheless, the new results sometimes are even better.

Note that all ResNet models were trained using [MXNet branch](https://github.com/saic-vul/fbrs_interactive_segmentation/tree/mxnet) and then converted to PyTorch (they have equivalent results). We provide the [script](./scripts/convert_weights_mx2pt.py) that was used to convert the models. HRNet models were trained using PyTorch.

You can find model weights and test results in the tables below:

<table>
  <tr>
    <th>Backbone</th>
    <th>Train Dataset</th>
    <th>Link</th>
  </tr>
  <tr>
    <td>ResNet-34</td>
    <td>SBD</td>
    <td><a href="https://github.com/saic-vul/fbrs_interactive_segmentation/releases/download/v1.0/resnet34_dh128_sbd.pth">resnet34_dh128_sbd.pth (GitHub, 89 MB)</a></td>
  </tr>
  <tr>
    <td>ResNet-50</td>
    <td>SBD</td>
    <td><a href="https://github.com/saic-vul/fbrs_interactive_segmentation/releases/download/v1.0/resnet50_dh128_sbd.pth">resnet50_dh128_sbd.pth (GitHub, 120 MB)</a></td>
  </tr>
  <tr>
    <td>ResNet-101</td>
    <td>SBD</td>
    <td><a href="https://github.com/saic-vul/fbrs_interactive_segmentation/releases/download/v1.0/resnet101_dh256_sbd.pth">resnet101_dh256_sbd.pth (GitHub, 223 MB)</a></td>
  </tr>
  <tr>
    <td>HRNetV2-W18+OCR</td>
    <td>SBD</td>
    <td><a href="https://github.com/saic-vul/fbrs_interactive_segmentation/releases/download/v1.0/hrnet18_ocr64_sbd.pth">hrnet18_ocr64_sbd.pth (GitHub, 39 MB)</a></td>
  </tr>
  <tr>
    <td>HRNetV2-W32+OCR</td>
    <td>SBD</td>
    <td><a href="https://github.com/saic-vul/fbrs_interactive_segmentation/releases/download/v1.0/hrnet32_ocr128_sbd.pth">hrnet32_ocr128_sbd.pth (GitHub, 119 MB)</a></td>
  </tr>
  <tr>
    <td>ResNet-50</td>
    <td>COCO+LVIS</td>
    <td><a href="https://github.com/saic-vul/fbrs_interactive_segmentation/releases/download/v1.0/resnet50_dh128_lvis.pth">resnet50_dh128_lvis.pth (GitHub, 120 MB)</a></td>
  </tr>
  <tr>
    <td>HRNetV2-W32+OCR</td>
    <td>COCO+LVIS</td>
    <td><a href="https://github.com/saic-vul/fbrs_interactive_segmentation/releases/download/v1.0/hrnet32_ocr128_lvis.pth">hrnet32_ocr128_lvis.pth (GitHub, 119 MB)</a></td>
  </tr>
</table>

<table align="center">
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2"><span style="font-weight:bold">BRS</span><br><span style="font-weight:bold">Type</span></th>
    <th colspan="2">GrabCut</th>
    <th colspan="2">Berkeley</th>
    <th colspan="2">DAVIS</th>
    <th colspan="2">SBD</th>
    <th colspan="2">COCO_MVal</th>
  </tr>
  <tr>
    <td>NoC<br>85%</td>
    <td>NoC<br>90%</td>
    <td>NoC<br>85%</td>
    <td>NoC<br>90%</td>
    <td>NoC<br>85%</td>
    <td>NoC<br>90%</td>
    <td>NoC<br>85%</td>
    <td>NoC<br>90%</td>
    <td>NoC<br>85%</td>
    <td>NoC<br>90%</td>
  </tr>

  <tr>
    <td rowspan="2">ResNet-34<br>(SBD)</td>
    <td>RGB-BRS</td>
    <td>2.04</td>
    <td>2.50</td>
    <td>2.22</td>
    <td>4.49</td>
    <td>5.34</td>
    <td>7.91</td>
    <td>4.19</td>
    <td>6.83</td>
    <td>4.16</td>
    <td>5.52</td>
  </tr>

  <tr>
    <td>f-BRS-B</td>
    <td>2.06</td>
    <td>2.48</td>
    <td>2.40</td>
    <td>4.17</td>
    <td>5.34</td>
    <td>7.73</td>
    <td>4.47</td>
    <td>7.28</td>
    <td>4.31</td>
    <td>5.79</td>
  </tr>

  <tr>
    <td rowspan="2">ResNet-50<br>(SBD)</td>
    <td>RGB-BRS</td>
    <td>2.16</td>
    <td>2.56</td>
    <td>2.17</td>
    <td>4.27</td>
    <td>5.27</td>
    <td>7.51</td>
    <td>4.00</td>
    <td>6.59</td>
    <td>4.12</td>
    <td>5.61</td>
  </tr>

  <tr>
    <td>f-BRS-B</td>
    <td>2.20</td>
    <td>2.64</td>
    <td>2.17</td>
    <td>4.22</td>
    <td>5.44</td>
    <td>7.81</td>
    <td>4.55</td>
    <td>7.45</td>
    <td>4.31</td>
    <td>6.26</td>
  </tr>

  <tr>
    <td rowspan="2">ResNet-101<br>(SBD)</td>
    <td>RGB-BRS</td>
    <td>2.10</td>
    <td>2.46</td>
    <td>2.34</td>
    <td>3.91</td>
    <td>5.19</td>
    <td><b>7.23</b></td>
    <td>3.78</td>
    <td><b>6.28</b></td>
    <td>3.98</td>
    <td>5.45</td>
  </tr>

  <tr>
    <td>f-BRS-B</td>
    <td>2.30</td>
    <td>2.68</td>
    <td>2.61</td>
    <td>4.22</td>
    <td>5.32</td>
    <td><b>7.35</b></td>
    <td>4.20</td>
    <td>7.10</td>
    <td>4.11</td>
    <td>5.91</td>
  </tr>

  <tr>
    <td rowspan="2">HRNet-W18+OCR<br>(SBD)</td>
    <td>RGB-BRS</td>
    <td>1.68</td>
    <td><b>1.94</b></td>
    <td>1.99</td>
    <td>3.81</td>
    <td>5.49</td>
    <td>7.98</td>
    <td>4.19</td>
    <td>6.84</td>
    <td>3.62</td>
    <td><b>5.04</b></td>
  </tr>

  <tr>
    <td>f-BRS-B</td>
    <td>1.86</td>
    <td>2.18</td>
    <td>2.07</td>
    <td>3.96</td>
    <td>5.62</td>
    <td>8.08</td>
    <td>4.70</td>
    <td>7.65</td>
    <td>3.87</td>
    <td>5.57</td>
  </tr>

  <tr>
    <td rowspan="2">HRNet-W32+OCR<br>(SBD)</td>
    <td>RGB-BRS</td>
    <td>1.80</td>
    <td>2.16</td>
    <td>2.00</td>
    <td><b>3.58</b></td>
    <td>5.40</td>
    <td>7.59</td>
    <td>3.87</td>
    <td><b>6.33</b></td>
    <td>3.61</td>
    <td><b>5.12</b></td>
  </tr>

  <tr>
    <td>f-BRS-B</td>
    <td>1.78</td>
    <td>2.16</td>
    <td>2.13</td>
    <td><b>3.69</b></td>
    <td>5.54</td>
    <td>7.62</td>
    <td>4.31</td>
    <td>7.08</td>
    <td>3.82</td>
    <td>5.44</td>
  </tr>

  <tr>
    <td class="divider" colspan="12"><hr /></td>
  </tr>

  <tr>
    <td rowspan="2">ResNet-50<br>(COCO+LVIS)</td>
    <td>RGB-BRS</td>
    <td>1.54</td>
    <td>1.76</td>
    <td>1.56</td>
    <td>2.70</td>
    <td>4.93</td>
    <td><b>6.22</b></td>
    <td>4.04</td>
    <td><b>6.85</b></td>
    <td>2.41</td>
    <td><b>3.47</b></td>
  </tr>

  <tr>
    <td>f-BRS-B</td>
    <td>1.52</td>
    <td>1.74</td>
    <td>1.56</td>
    <td>2.61</td>
    <td>4.94</td>
    <td><b>6.36</b></td>
    <td>4.29</td>
    <td><b>7.20</b></td>
    <td>2.34</td>
    <td><b>3.43</b></td>
  </tr>

  <tr>
    <td rowspan="2">HRNet-W32+OCR<br>(COCO+LVIS)</td>
    <td>RGB-BRS</td>
    <td>1.54</td>
    <td><b>1.60</b></td>
    <td>1.63</td>
    <td><b>2.59</b></td>
    <td>5.06</td>
    <td>6.34</td>
    <td>4.18</td>
    <td>6.96</td>
    <td>2.38</td>
    <td>3.55</td>
  </tr>

  <tr>
    <td>f-BRS-B</td>
    <td>1.54</td>
    <td><b>1.69</b></td>
    <td>1.64</td>
    <td><b>2.44</b></td>
    <td>5.17</td>
    <td>6.50</td>
    <td>4.37</td>
    <td>7.26</td>
    <td>2.35</td>
    <td>3.44</td>
  </tr>

</table>

## Citation

```
@inproceedings{fbrs2020,
   title={f-brs: Rethinking backpropagating refinement for interactive segmentation},
   author={Sofiiuk, Konstantin and Petrov, Ilia and Barinova, Olga and Konushin, Anton},
   booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
   pages={8623--8632},
   year={2020}
}
```
