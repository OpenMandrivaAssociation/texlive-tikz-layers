%global tl_name tikz-layers
%global tl_revision 46660

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9
Release:	%{tl_revision}.1
Summary:	TikZ provides graphical layers on TikZ: behind, above and glass
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-layers
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-layers.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-layers.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TikZ-layers is a tiny package that provides, along side "background",
typical graphical layers on TikZ: "behind", "above" and "glass". The
layers may be selected with one of the styles "on behind layer", "on
above layer", "on glass layer" as an option to a {scope} environment.

