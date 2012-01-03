# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-construction-plan
# catalog-date 2008-08-18 23:54:09 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-construction-plan
Version:	20080818
Release:	2
Summary:	Construction plans in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-construction-plan
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-construction-plan.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-construction-plan.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
Generate a page with a figure at a well-defined scale.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/construction-plan/t-construction-plan.tex
%doc %{_texmfdistdir}/doc/context/third/construction-plan/construction-plan-demo.pdf
%doc %{_texmfdistdir}/doc/context/third/construction-plan/construction-plan-doc.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
