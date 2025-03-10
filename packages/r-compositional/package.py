# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompositional(RPackage):
	"""Compositional Data Analysis

	Regression, classification, contour plots, hypothesis testing and fitting of distributions for compositional data are some of the functions included. We further include functions for percentages (or proportions).
             The standard textbook for such data is John Aitchison's (1986) "The statistical analysis of compositional data". Relevant papers include:
			       a) Tsagris M.T., Preston S. and Wood A.T.A. (2011). "A data-based power transformation for compositional data". Fourth International International Workshop on Compositional Data Analysis. 
			       b) Tsagris M. (2014). "The k-NN algorithm for compositional data: a revised approach with and without zero values present". Journal of Data Science, 12(3): 519--534. 
			       c) Tsagris M. (2015). "A novel, divergence based, regression for compositional data". Proceedings of the 28th Panhellenic Statistics Conference, 15-18 April 2015, Athens, Greece, 430--444. 
			       d) Tsagris M. (2015). "Regression analysis with compositional data containing zero values". Chilean Journal of Statistics, 6(2): 47--57. 
			       e) Tsagris M., Preston S. and Wood A.T.A. (2016). "Improved supervised classification for compositional data using the alpha-transformation". Journal of Classification, 33(2): 243--261. <doi:10.1007/s00357-016-9207-5>. 
			       f) Tsagris M., Preston S. and Wood A.T.A. (2017). "Nonparametric hypothesis testing for equality of means on the simplex". Journal of Statistical Computation and Simulation, 87(2): 406--422. <doi:10.1080/00949655.2016.1216554>. 
			       g) Tsagris M. and Stewart C. (2018). "A Dirichlet regression model for compositional data with zeros". Lobachevskii Journal of Mathematics, 39(3): 398--412. <doi:10.1134/S1995080218030198>. 
			       h) Alenazi A. (2019). "Regression for compositional data with compositional data as predictor variables with or without zero values". Journal of Data Science, 17(1): 219--238. <doi:10.6339/JDS.201901_17(1).0010>. 
		         i) Tsagris M. and Stewart C. (2020). "A folded model for compositional data analysis". Australian and New Zealand Journal of Statistics, 62(2): 249--277. <doi:10.1111/anzs.12289>. 
		         j) Alenazi A. (2021). Alenazi, A. (2023). "A review of compositional data analysis and recent advances". Communications in Statistics--Theory and Methods, 52(16): 5535--5567. <doi:10.1080/03610926.2021.2014890>.
		         k) Alenazi A.A. (2022). "f-divergence regression models for compositional data". Pakistan Journal of Statistics and Operation Research, 18(4): 867--882. <doi:10.18187/pjsor.v18i4.3969>.
		         l) Tsagris M. and Stewart C. (2022). "A Review of Flexible Transformations for Modeling Compositional Data". In Advances and Innovations in Statistics and Data Science, pp. 225--234. <doi:10.1007/978-3-031-08329-7_10>.
			       m) Tsagris M., Alenazi A. and Stewart C. (2023). "Flexible non-parametric regression models for compositional response data with zeros". Statistics and Computing, 33(106). <doi:10.1007/s11222-023-10277-5>. 
	"""
	
	cran = "Compositional" 

	version("6.6", md5="2b8d2453425c13777566b830145d572d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-codalm", type=("build", "run"))
	depends_on("r-directional", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-emplik", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-flexdir", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mda", type=("build", "run"))
	depends_on("r-mixture", type=("build", "run"))
	depends_on("r-mvhtests", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pchc", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-regda", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
	depends_on("r-rnanoflann", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
