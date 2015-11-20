sendid="$HOSTNAME/test"
monserver=faihost
FAI_MONITOR_PORT=4711

sendmon() {
    # send message to monitor daemon
    #echo "$*" >> $LOGDIR/fai-monitor.log
    #[ "$faimond" -eq 0 ] && return 0
    echo "$sendid $*" | nc -w 8 $monserver $FAI_MONITOR_PORT 2>/dev/null
    return $?
}

sendmon "foo"
