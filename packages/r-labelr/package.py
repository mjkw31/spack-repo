# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabelr(RPackage):
	"""Label Data Frames, Variables, and Values

	Create and use data frame labels for data frame objects (frame labels), their columns (name labels), and individual values of a column (value labels). Value labels include one-to-one and many-to-one labels for nominal and ordinal variables, as well as numerical range-based value labels for continuous variables. Convert value-labeled variables so each value is replaced by its corresponding value label. Add values-converted-to-labels columns to a value-labeled data frame while preserving parent columns. Filter and subset a value-labeled data frame using labels, while returning results in terms of values. Overlay labels in place of values in common R commands to increase interpretability. Generate tables of value frequencies, with categories expressed as raw values or as labels. Access data frames that show value-to-label mappings for easy reference.
	"""
	
	cran = "labelr" 

	version("0.1.2", md5="808f301e4fa86c4a0078378fd33fc352")

	depends_on("r@4:", type=("build", "run"))
