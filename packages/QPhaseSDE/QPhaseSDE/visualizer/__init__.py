"""
QPhaseSDE: Visualizers Subpackage
---------------------------------
Figure plotters and services for simulation outputs (phase portraits, PSD),
validated by specs and plugged via the central registry.

Usage
-----
Registry keys:
`visualizer:phase_portrait` | `visualizer:psd`

Service:
>>> from QPhaseSDE.visualizer.service import render_from_spec

Notes
-----
- Renderers are registered lazily; plotting dependencies are imported only
  when needed.
"""

from ..core.registry import register_lazy

# Phase portrait renderer (function). We return the callable rather than
# instantiating anything at registration time.
register_lazy(
	"visualizer",
	"phase_portrait",
	"QPhaseSDE.visualizer.plotters.phase_plane:render_phase_portrait",
	return_callable=True,
)

# Power Spectral Density renderer
register_lazy(
	"visualizer",
	"psd",
	"QPhaseSDE.visualizer.plotters.psd:render_psd",
	return_callable=True,
)

__all__ = []
