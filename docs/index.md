# kplot

This library is used to draw figures for papers using the matplotlib module.

matplotlibを使った論文作成時に使えそうなシンプルなグラフやヒストグラムを書く事ができる、かゆいところに手が届くライブラリです。

![Static Badge](https://img.shields.io/badge/release-v%20b.1.0-yellow)
![Static Badge](https://img.shields.io/badge/python-%3E%3D3.9-blue)
![Static Badge](https://img.shields.io/badge/license-MIT-blue)

## demo sample

- Scatter2D (scatter mode)

<img alt="kamioka-data-SN1987A" src="https://github.com/kyasya/kplot/blob/main/image/kamioka-SN1987A-demo.png" width="600">

- From Tab.1 and Fig.3 data of Kamiokande experiment in ref: [K. Hirata, Phys. Rev. Lett. 58, 1490](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.58.1490 )


## How to install

1. clone this repository.

    ```bash
    ~$ cd [work path]
    [work path]$ git clone https://github.com/kyasya/kplot.git
    ```

2. open the terminal, and change to `src` directory under the installed repository.

    ```bash
    [work path]$ cd src
    ```

3. install using `src` command.: 

    ```bash
    [work path]/bin$ pip install .
    ```

4. Installation check. You can use the [demo programs](#demo-sample). (./samples)

## Note

This software is developing as the **beta version**. The program works correctly, however we have not optimized the function. We plan to support this in the next version.

## how to use

see the reference.

### histogram

```python
import numpy as np
import kplot

# data
x = np.random.normal(0, 1, 1000)

# plot
h = kplot.hist('Title;x;Events', 100, -5, 5)
h.Draw1D(x)
```
<img alt="Image" src="https://github.com/kyasya/kplot/blob/main/image/demo-hist1D.png" width="600">

### Separated graph

- This is useful when drawing a graph of the fitting.

**NOTE**: Filling in the fitting caves requires a graph to be obtained. Fitting functionality will be added in the future.

<img alt="Image" src="https://github.com/kyasya/kplot/blob/main/image/demo-sep2graph.png" width="600">

### 2D scatter/hist

- mode change to scatter/hist.

```python
# data
x = np.random.normal(0, 0.7, 1000)
y = np.random.normal(0, 0.8, 1000)

# plot histogram
h = kplot.scatter3(100, -5, 5, 100, -5, 5, figsize=(6,6))
h.Draw(x, y, mode='hist') 
h.SetxLimit(-3, 3)
h.SetyLimit(-3, 3)
h.SetxLabel('x')
h.SetyLabel('y')

h.Print('./demo-hist2D.png')
```

- hist mode (`mode` parameter set to be `'hist'`)

<img alt="Image" src="https://github.com/kyasya/kplot/blob/main/image/demo-hist2D-hist.png" width="500">

- scatter mode (`mode` parameter set to be `'scatter'`)

<img alt="Image" src="https://github.com/kyasya/kplot/blob/main/image/demo-hist2D-scatter.png" width="500">

## License

We use [the MIT License](https://opensource.org/license/mit).
