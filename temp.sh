
N=100000
hits=(0 0 0 0) # initialize hit counters
if [ $# -gt 0 ]; then
# check whether there is an argument
N=$1
else
# ask for the number if no argument
echo "Enter the number of trials: "
TMOUT=5
# 5 seconds to give the input
read N
fi
i=$N
echo "Generating $N random numbers... please wait."
SECONDS=0
# here is where we really start
while [ $i -gt 0 ]; do # run until the counter gets to zero
case $((RANDOM%4)) in
# randmize from 0 to 3
0) let "hits[0]+=1";;
# count the hits
1) let "hits[1]=${hits[1]}+1";;
2) let hits[2]=$((${hits[2]}+1));;
3) let hits[3]=$((${hits[3]}+1));;
esac
let "i-=1"
done
echo "Probabilities of drawing a specific color:"
# use bc - bash does not support fractions
echo "Clubs: " `echo ${hits[0]}*100/$N | bc -l`
echo "Diamonds: " `echo ${hits[1]}*100/$N | bc -l`
echo "Hearts: " `echo ${hits[2]}*100/$N | bc -l`
echo "Spades: " `echo ${hits[3]}*100/$N | bc -l`
echo "=========================================="
echo "Execution time: $SECONDS"
