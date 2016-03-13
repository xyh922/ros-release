Name:           ros-kinetic-ros
Version:        1.13.1
Release:        0%{?dist}
Summary:        ROS ros package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ROS
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-catkin
Requires:       ros-kinetic-mk
Requires:       ros-kinetic-rosbash
Requires:       ros-kinetic-rosboost-cfg
Requires:       ros-kinetic-rosbuild
Requires:       ros-kinetic-rosclean
Requires:       ros-kinetic-roscreate
Requires:       ros-kinetic-roslang
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rosmake
Requires:       ros-kinetic-rosunit
BuildRequires:  ros-kinetic-catkin

%description
ROS packaging system

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Mar 13 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.1-0
- Autogenerated by Bloom

* Thu Mar 10 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.0-0
- Autogenerated by Bloom

