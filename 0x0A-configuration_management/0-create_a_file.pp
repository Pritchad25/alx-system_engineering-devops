# This puppet manifest creates a file with specific permissions.

file { '/tmp/school':
ensure => 'file',
mode   => '0744',
owner  => 'www-data',
group  => 'www-data',
content => 'I love Puppet',
}
