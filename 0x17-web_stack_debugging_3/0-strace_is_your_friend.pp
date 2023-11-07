# Fixing the issue that causes Apache to return a 500 error
file { ‘/etc/profile.d/custom_ld_library_path.sh’:

ensure => present,

content => ‘export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/libfoo’,

mode => ‘0644’,

}

# Restarting the Apache Service

service { ‘apache2’:

ensure => running,

subscribe => File[‘/etc/profile.d/custom_ld_library_path.sh’],

}
