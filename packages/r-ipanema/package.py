# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpanema(RPackage):
	"""Read Data from 'LimeSurvey'

	Read data from 'LimeSurvey'
    (<https://www.limesurvey.org/>)
    in a comfortable way.
    Heavily inspired by 'limer'
    (<https://github.com/cloudyr/limer/>),
    which lacked a few comfort features for me.
	"""
	
	homepage = "https://gitlab.com/REDS1736/ipanema"
	cran = "ipanema" 

	version("0.6.7", md5="0fb4cd8f6728cbba3c9f15cbb27c8c77")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rmysql", type=("build", "run"))
