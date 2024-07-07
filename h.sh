#!/bin/bash
#xkill -id `xprop -root _NET_ACTIVE_WINDOW | cut -d\# -f2`

#run app

python e.py & 
python rus2.py &

# Get the initial positions of both windows
POSTX=$(wmctrl -l -G | grep "Transparent Window" | awk '{print $3}')
POSTY=$(wmctrl -l -G | grep "Transparent Window" | awk '{print $4}')
POSHX=$(wmctrl -l -G | grep "Hellper_2.0" | awk '{print $3}')
POSHY=$(wmctrl -l -G | grep "Hellper_2.0" | awk '{print $4}')

# Monitor for changes in the position of Hellper_2.0
while true; do

  # Check if Hellper_2.0 has moved
  NEW_POSH=$(wmctrl -l -G | grep "Hellper_2.0" | awk '{print $3,$4}')

  x=$(echo "$NEW_POSH" | cut -d' ' -f1)
  y=$(echo "$NEW_POSH" | cut -d' ' -f2)
  if [ "$x $y" != "$POSHX $POSHY" ]; then


    # Update the position of Transparent Window with the same absolute coordinates as Hellper_2.0
    POSTX=$(( x + 470 ))
    POSTY=$(( y + 12 ))

    # Move Transparent Window to new position
    wmctrl -r "Transparent Window" -e 0,$POSTX,$POSTY,488,276

    POSHX=$(( x + 470 ))
    POSHY=$(( y + 12 ))
  fi
  sleep 0.1 # wait 0.5 seconds before checking again
done

