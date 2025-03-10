# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStruct(RPackage):
	"""Statistics in R Using Class-based Templates

	Defines and includes a set of class-based templates for developing and implementing data processing and analysis workflows, with a strong emphasis on statistics and machine learning. The templates can be used and where needed extended to 'wrap' tools and methods from other packages into a common standardised structure to allow for effective and fast integration. Model objects can be combined into sequences, and sequences nested in iterators using overloaded operators to simplify and improve readability of the code. Ontology lookup has been integrated and implemented to provide standardised definitions for methods, inputs and outputs wrapped using the class-based templates.
	"""
	
	bioc = "struct" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/struct_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/struct/struct_1.14.0.tar.gz"]

	version("1.14.0", md5="ef5fb8febc9f7bfed87fba9bc24cbebc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rols", type=("build", "run"))
