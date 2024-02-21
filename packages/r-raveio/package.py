# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaveio(RPackage):
	"""File-System Toolbox for RAVE Project

	Includes multiple cross-platform read/write interfaces for
	'RAVE' project. 'RAVE' stands for "R analysis and visualization of human 
	intracranial electroencephalography data". The whole project aims at 
	providing powerful free-source package that analyze brain recordings from 
	patients with electrodes placed on the cortical surface or inserted into 
	the brain. 'raveio' as part of this project provides tools to read/write 
	neurophysiology data from/to 'RAVE' file structure, as well as several 
	popular formats including  'EDF(+)', 'Matlab', 'BIDS-iEEG', and 'HDF5', 
	etc. Documentation and examples about 'RAVE' project are provided at 
	<https://openwetware.org/wiki/RAVE>, and the paper by John F. Magnotti, 
	Zhengjia Wang, Michael S. Beauchamp (2020) 
	<doi:10.1016/j.neuroimage.2020.117341>; see 'citation("raveio")' for 
	details.
	"""
	
	homepage = "https://beauchamplab.github.io/raveio/"
	cran = "raveio"

	version("0.9.0", md5="77f88721025135fa4c7661bde3e8cf10")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-edfreader@1.2.1:", type=("build", "run"))
	depends_on("r-dipsaus", type=("build", "run"))
	depends_on("r-filearray@0.1.3:", type=("build", "run"))
	depends_on("r-fst@0.9.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-globals", type=("build", "run"))
	depends_on("r-hdf5r@1.3.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-r-matlab@3.6.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-yaml@2.2.1:", type=("build", "run"))
	depends_on("r-targets@0.8:", type=("build", "run"))
	depends_on("r-callr@3.7:", type=("build", "run"))
	depends_on("r-remotes@2.1.2:", type=("build", "run"))
	depends_on("r-promises@1.2:", type=("build", "run"))
	depends_on("r-threebrain@0.2.5:", type=("build", "run"))
	depends_on("r-rpymat", type=("build", "run"))
	depends_on("r-ravetools", type=("build", "run"))
