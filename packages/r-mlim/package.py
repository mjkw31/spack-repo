# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlim(RPackage):
	"""Single and Multiple Imputation with Automated Machine Learning

	Machine learning algorithms have been used for performing 
    single missing data imputation and most recently, multiple imputations. 
    However, this is the first attempt for using automated machine learning algorithms 
    for performing both 
    single and multiple imputation. Automated machine learning is a procedure for 
    fine-tuning the model automatic, performing a random search for a model that 
    results in less error, without overfitting the data. The main idea is 
    to allow the model to set its own parameters for imputing each variable separately 
    instead of setting fixed predefined parameters to impute all variables 
    of the dataset.
    Using automated machine learning, the package fine-tunes an Elastic 
    Net (default) or Gradient Boosting, Random Forest, Deep Learning, Extreme Gradient Boosting,
    or Stacked Ensemble machine learning model (from one or a combination of other 
    supported algorithms) for imputing the missing 
    observations. This procedure has been implemented for the 
    first time by this package and is expected to outperform other packages for 
    imputing missing data that do not fine-tune their models. The multiple imputation 
    is implemented via bootstrapping without letting the duplicated observations to 
    harm the cross-validation procedure, which is the way imputed variables are evaluated.
    Most notably, the package implements automated procedure for handling imputing imbalanced 
    data (class rarity problem), which happens when a factor variable has a level that is far more 
    prevalent than the other(s). This is known to result in biased predictions, hence, biased 
    imputation of missing data. However, the autobalancing procedure ensures that instead of 
    focusing on maximizing accuracy (classification error) in imputing factor variables, 
    a fairer procedure and imputation method is practiced. 
	"""
	
	homepage = "https://github.com/haghish/mlim"
	cran = "mlim" 

	version("0.3.0", md5="d9345a31256c27d0b0383a19576e69bd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-h2o@3.34:", type=("build", "run"))
	depends_on("r-curl@4.3.2:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-missranger", type=("build", "run"))
	depends_on("r-memuse", type=("build", "run"))
	depends_on("r-md-log@0.2:", type=("build", "run"))
