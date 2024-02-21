# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThreebrain(RPackage):
	"""3D Brain Visualization

	A fast, interactive cross-platform, and easy to share 
    'WebGL'-based 3D brain viewer that visualizes 'FreeSurfer' and/or
    'AFNI/SUMA' surfaces. The viewer widget can be either standalone or 
    embedded into 'R-shiny' applications. The standalone version only require
    a web browser with 'WebGL2' support (for example, 'Chrome', 'Firefox', 
    'Safari'), and can be inserted into any websites. The 'R-shiny' 
    support allows the 3D viewer to be dynamically generated from reactive user 
    inputs. This feature has been fully adopted by 'RAVE' 
    <https://openwetware.org/wiki/RAVE>, an interactive toolbox to 
    analyze 'iEEG' data. Documentation about 'threeBrain' is provided
    by <https://dipterix.org/threeBrain/> and several vignettes included 
    in this package. To cite the package, please check our 'NeuroImage' paper 
    by Magnotti, Wang, and Beauchamp (2020, <doi:10.1016/j.neuroimage.2020.117341>),
    or see 'citation("threeBrain")' for details.
	"""
	
	homepage = "https://dipterix.org/threeBrain/"
	cran = "threeBrain" 

	version("1.0.1", md5="453d74a4079ea74fc8796071d2ac7e46")

	depends_on("r-dipsaus", type=("build", "run"))
	depends_on("r-ravetools", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-servr", type=("build", "run"))
	depends_on("r-shiny@1.2:", type=("build", "run"))
	depends_on("r-digest@0.6.22:", type=("build", "run"))
	depends_on("r-freesurferformats@0.1.7:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.3:", type=("build", "run"))
	depends_on("r-r6@2.3:", type=("build", "run"))
	depends_on("r-gifti@0.7.5:", type=("build", "run"))
	depends_on("r-oro-nifti@0.9.1:", type=("build", "run"))
