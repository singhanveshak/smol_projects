#!/bin/bash

#purpose of script = solve basic CTF problems
#author = Anveshak Singh
#date = Mon, Oct 2, 2023
#contact = anveshaksingh123@gmail.com

#echo;echo 'AWESOME RESOURCES THAT MAKE LIFE EASIER:'
#echo '1. cyberchef from github https://gchq.github.io/CyberChef/'; echo "2. https://md5.gromweb.com/ ";echo "https://sha1.gromweb.com/"; echo "https://md5hashing.net/hash"


echo "
			⠀⠀⠀⠀⠀⠀⢀⣀⣀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
			⢰⡄⠀⠀⣠⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
			⢸⡇⠐⠾⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
			⠀⡇⠀⢠⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
			⠐⣿⣾⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
			⠀⢹⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⣄⠀⢻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
			⠀⢸⠈⠉⣿⣿⣿⣿⣿⣿⡄⠀⢸⣤⣼⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀
			⠀⠸⡆⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⢏⠙⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
			⠀⠀⠇⢀⣿⣿⣿⣿⣿⣿⣿⣧⡀⠸⡀⣿⣿⣿⢆⠀⠀⠀⠀⠀⠀
			⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢣⠻⣟⠉⢻⣆⠀⠀⠀⠀⠀
			⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣷⣿⣶⣾⣷⣶⣦⡀⠀⠀
			⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡄ ~One Script to rule them all!
                       _____                 _       _  __
                      / ____|               | |     | |/ _|
                     | |  __  __ _ _ __   __| | __ _| | |_
                     | | |_ |/ _  | '_ \ / _   / _  | |  _|
                     | |__| | (_| | | | | (_| | (_| | | |
                      \_____|\__,_|_| |_|\__,_|\__,_|_|_|

"

pic=$1

#-----------------------------------OPTIONS-------------------------------------
echo "Whats your purpose?
stegno (s)		crypto (c)		reversing (r)		help(h)"
read option
case $option in
    
    "s")
        
        #---------------------------------STEGNOGRAPHY (s)------------------------------
        #HANDLING IMAGES
        echo "binwalk? (y/n)"
        read choice
        if [ $choice = "y"  ];then
            binwalk $pic; echo
        fi
        
        echo "foremost? (y/n)"
        read choice
        if [ $choice = "y"  ];then
            foremost $pic
            echo; echo "foremost written to 'output' dir"
        fi
        
        echo "strings? (y/n)"
        read choice
        if [ $choice = "y"  ];then
            strings $pic | cat > strout
            echo; echo "strings written to 'strout' file"; echo
        fi
        
        echo "stegsolve? (y/n)"
        read choice
        if [ $choice = "y"  ];then
            java -jar /usr/bin/stegsolve.jar $pic
            echo; echo;
        fi
        
        echo "exiftool? (y/n)"
        read choice
        if [ $choice = "y"  ];then
            exiftool $pic
            echo;
        fi
        
        echo "zsteg? (only works for .png .bmp) (y/n)"
        read choice
        if [ $choice = "y"  ];then
            zsteg $pic; echo
        fi
        
        echo "steghide extract? (y/n)"
        read choice
        if [ $choice = "y"  ];then
            steghide extract -sf $pic; echo
        fi
        
        echo "stegseek with rockyou.txt? (y/n)"
        read choice
        if [ $choice = "y"  ];then
        	stegseek $pic /usr/bin/common-password-list/rockyou.txt/rockyou.txt
        fi
        
        echo "stegsnow? (y/n)"
        read choice
        if [ $choice = "y"  ];then
            stegsnow -C $pic; echo
        fi
        
        
        #HANDLING PDFs
        echo "NOW IF IT IS A PDF, WHICH COMMANDS WOULD YOU LIKE TO USE? (Enter commands seperated by spaces)"
        echo "pdf2dsc      pdfdetach    pdfinfo      pdftocairo   pdftops
pdf2ps       pdffonts     pdfseparate  pdftohtml    pdftotext
pdfattach    pdfimages    pdfsig       pdftoppm     pdfunite"
        
    ;;
    
    "r")
        
        #-------------------------------------REVERSING-----------------------------------------
        #HANDLING ASSEMBLY
        echo "NOW IF IT IS AN ASSEMBLY WOULD YOU LIKE TO 'objdump'? (y/n)"
        read choice
        if [ $choice = "y"  ];then
            echo "Attempting disassembly of $1 ..."
            
            #This usage of "objdump" disassembles all (-D) of the first file given by
            #invoker, but only prints out the ".text" section (-j .text) (only section
            #that matters in almost any compiled program...
            
            objdump -Dj .text $1 > $1.ltdis.x86_64.txt
            
            #Check that $1.ltdis.x86_64.txt is non-empty
            #Continue if it is, otherwise print error and eject
            
            if [ -s "$1.ltdis.x86_64.txt" ]
            then
                echo "Disassembly successful! Available at: $1.ltdis.x86_64.txt"
                
                echo "Ripping strings from binary with file offsets..."
                strings -a -t x $1 > $1.ltdis.strings.txt
                echo "Any strings found in $1 have been written to $1.ltdis.strings.txt with file offset"
            else
                echo;echo "Disassembly failed!"
                echo "Bye!"
            fi
        fi
        
    ;;
    
    "c")
        
        #---------------------------------CRYPTOGRAPHY-----------------------------------------------
        
        echo "identify hash type (with hashid)? (y/n)"
        read choice
        if [ $choice = "y"  ];then
            echo "enter hash: ";read hash
            hashid $hash; echo
        fi
                
        retry="y"
        flag=0
        while [ $retry = "y" ];do

        echo "decrypt hash (with hashcat+rockyou.txt)? (y/n)"
        read choice
        if [ $choice = "y"  ];then
        	echo "enter the type of hash (sha/sha1/sha2/md5/cisco): "; read type
        	            hashcat --help | grep -i $type
        	            if [ $? -ne 0 ];then
							echo "			BAD CHOICE"
            			fi
            echo "Select hash type number from the list above: "; read num
            
            if [ $flag -eq 0 ];then
            echo "Now enter hash: "; read hash; echo $hash | cat > hash.txt; flag=1; fi
     		hashcat -m $num --show hash.txt /usr/bin/common-password-list/rockyou.txt/rockyou.txt
     		hashcat -m $num hash.txt /usr/bin/common-password-list/rockyou.txt/rockyou.txt
        fi
        echo;echo "RETRY with a different hash type (and same hash)? (y/n)";read retry                
    	
    	done
    	rm hash.txt 
    ;;
    
    "h")
        
        echo;echo "		USAGE: ./gandalf.sh [filename]"
        echo;echo "Do you want to enter the filename start fresh? (y/n)"
        read yn
        
        if [ $yn = "y" ];then
            clear
            echo "Enter relative file path: "
            read file
            ./gandalf.sh $file
        fi
    ;;
esac

