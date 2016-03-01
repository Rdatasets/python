"""
Hair and Eye Color of Statistics Students
-----------------------------------------

Description
~~~~~~~~~~~

Distribution of hair and eye color and sex in 592 statistics students.

R - Usage
~~~~~~~~~

::

    HairEyeColor

Format
~~~~~~

A 3-dimensional array resulting from cross-tabulating 592 observations
on 3 variables. The variables and their levels are as follows:

+------+--------+-----------------------------+
| No   | Name   | Levels                      |
+------+--------+-----------------------------+
| 1    | Hair   | Black, Brown, Red, Blond    |
+------+--------+-----------------------------+
| 2    | Eye    | Brown, Blue, Hazel, Green   |
+------+--------+-----------------------------+
| 3    | Sex    | Male, Female                |
+------+--------+-----------------------------+

Details
~~~~~~~

The Hair *x* Eye table comes rom a survey of students at the University
of Delaware reported by Snee (1974). The split by ``Sex`` was added by
Friendly (1992a) for didactic purposes.

This data set is useful for illustrating various techniques for the
analysis of contingency tables, such as the standard chi-squared test
or, more generally, log-linear modelling, and graphical methods such as
mosaic plots, sieve diagrams or association plots.

Source
~~~~~~

`http://euclid.psych.yorku.ca/ftp/sas/vcd/catdata/haireye.sas <http://euclid.psych.yorku.ca/ftp/sas/vcd/catdata/haireye.sas>`__

Snee (1974) gives the two-way table aggregated over ``Sex``. The ``Sex``
split of the ‘Brown hair, Brown eye’ cell was changed to agree with that
used by Friendly (2000).

References
~~~~~~~~~~

Snee, R. D. (1974) Graphical display of two-way contingency tables. *The
American Statistician*, **28**, 9–12.

Friendly, M. (1992a) Graphical methods for categorical data. *SAS User
Group International Conference Proceedings*, **17**, 190–200.
`http://www.math.yorku.ca/SCS/sugi/sugi17-paper.html <http://www.math.yorku.ca/SCS/sugi/sugi17-paper.html>`__

Friendly, M. (1992b) Mosaic displays for loglinear models. *Proceedings
of the Statistical Graphics Section*, American Statistical Association,
pp. 61–68.
`http://www.math.yorku.ca/SCS/Papers/asa92.html <http://www.math.yorku.ca/SCS/Papers/asa92.html>`__

Friendly, M. (2000) *Visualizing Categorical Data.* SAS Institute, ISBN
1-58025-660-0.

R - See Also
~~~~~~~~

``chisq.test``, ``loglin``, ``mosaicplot``

R - Examples
~~~~~~~~~~

::

    require(graphics)
    ## Full mosaic
    mosaicplot(HairEyeColor)
    ## Aggregate over sex (as in Snee's original data)
    x <- apply(HairEyeColor, c(1, 2), sum)
    x
    mosaicplot(x, main = "Relation between hair and eye color")

Python - Examples
~~~~~~~~~~~~~~~~~

::

    import hair_eye_color
    import matplotlib.pyplot as plt
    from statsmodels.graphics.mosaicplot import mosaic
    mosaic(hair_eye_color.data)
    plt.show()

Thanks to R core datasets
~~~~~~~~~~~~~~~~~~~~~~~~~

https://github.com/wch/r-source/blob/trunk/src/library/datasets/data/HairEyeColor.R

"""

import numpy as np
import xarray


data = np.array([32, 53, 10, 3, 11, 50, 10, 30, 10, 25, 7, 5, 3, 15, 7, 8,
                 36, 66, 16, 4,  9, 34,  7, 64,  5, 29, 7, 5, 2, 14, 7, 8])

_dim = (4, 4, 2)
data = data.reshape(_dim[::-1])

_dims = ['Hair', 'Eye', 'Sex']
_coords = [['Black', 'Brown', 'Red', 'Blond'], 
           ['Brown', 'Blue', 'Hazel', 'Green'],
           ['Male', 'Female']]

data = xarray.DataArray(
    data, dims=_dims[::-1],
    coords=_coords[::-1], name='Number'
)

assert int(data.loc['Female', 'Green', 'Black']) == 2
