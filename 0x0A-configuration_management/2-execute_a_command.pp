# This puppet manifest kills a process usig pkill

exec { 'kill_killmenow_process':
command     => 'pkill killmenow',
path        => '/usr/bin:/bin',
onlyif      => 'pgrep killmenow',
refreshonly => true,
}
