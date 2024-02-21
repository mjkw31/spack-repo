# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataset(RPackage):
	"""Create Data Frames that are Easier to Exchange and Reuse

	The aim of the 'dataset' package is to make tidy datasets easier to release, 
    exchange and reuse. It organizes and formats data frame 'R' objects into well-referenced, 
    well-described, interoperable datasets into release and reuse ready form. A subjective 
    interpretation of the  W3C  DataSet recommendation and the datacube model  <https://www.w3.org/TR/vocab-data-cube/>, 
    which is also used in the global Statistical Data and Metadata eXchange standards, 
    the application of the connected Dublin Core <https://www.dublincore.org/specifications/dublin-core/dcmi-terms/> 
    and DataCite <https://support.datacite.org/docs/datacite-metadata-schema-44/> standards 
    preferred by European open science repositories to improve the findability, accessibility,
    interoperability and reusability of the datasets.
	"""
	
	homepage = "https://github.com/dataobservatory-eu/dataset"
	cran = "dataset" 

	version("0.3.1", md5="a681e67563ba56013fe371f2dc752993")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-isocodes", type=("build", "run"))
