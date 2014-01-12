is_alive_ping()
{
  ping -c 1 $1 > /dev/null
  [ $? -eq 0 ] && echo $i
}
read -p "IP[1.2.3]" IP
for i in $IP.{1..254} 
do
is_alive_ping $i & disown
done
