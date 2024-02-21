# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadnsx(RPackage):
	"""Read 'Blackrock-Microsystems' Files ('NEV', 'NSx')

	Loads 'Blackrock' <https://blackrockneurotech.com> neural signal 
	data files into the memory, provides utility tools to extract the data into 
	common formats such as plain-text 'tsv' and 'HDF5'.
	"""
	
	homepage = "http://dipterix.org/readNSx/"
	cran = "readNSx"

	version("0.0.2", md5="08efa9e95004c28095b34c58afe9794e")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fastmap", type=("build", "run"))
	depends_on("r-hdf5r", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("hdf5@1.8.13:", type=("build", "link", "run"))
