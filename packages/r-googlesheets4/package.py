# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGooglesheets4(RPackage):
	"""Access Google Sheets using the Sheets API V4.

	Interact with Google Sheets through the Sheets API v4
	<https://developers.google.com/sheets/api>. "API" is an acronym for
	"application programming interface"; the Sheets API allows users to
	interact with Google Sheets programmatically, instead of via a web browser.
	The "v4" refers to the fact that the Sheets API is currently at version 4.
	This package can read and write both the metadata and the cell data in a
	Sheet."""

	cran = "googlesheets4"

	version("1.1.1", md5="8b017d8e142ceb41bd0baaee823a6508", url="https://cran.r-project.org/src/contrib/googlesheets4_1.1.1.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cellranger", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-gargle@1.5:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-googledrive@2.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-ids", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rematch2", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-vctrs@0.2.3:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
