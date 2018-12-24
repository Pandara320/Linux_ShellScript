#!/bin/bash
#Pandara320

#q1:
input=$1

#q2 create a trash directory under home if not exist
cd ~
if [ ! -d "$TRASH" ]
then
	cd ~
	mkdir TRASH
else
	echo "[Note]: the TRASH folder already exists"
fi
cd ~
tarName="$1.tar"
zipFileName="$1.gz"
zipFileName2="$1.tar.gz"
ExtendDate=$(date "+%m%d%y")
newzipFileName="$1$ExtendDate.gz"
newzipFileName2="$1$ExtendDate.tar.gz"
#q3: if  inputfile or directory exists in ~
if [ -e "$1" ]
then
	echo "[Note]: The commandLine input $1 exists "
	#q4: if file zipped
	numZip=$(file $1 | grep -c "compressed")

	# if file is not zipped, zipp the file with -r to recursively
	if [ $numZip -eq 0 ]
	then
		#check input's type is file or directory, zipp recusrsively based on type.
		if [[ -d $1 ]]; then
		    echo "[Note]: The commandline input $1 is a [Directory]"
				echo "[Note]: The original [Directory] $1 ----start ziping----"
				tar -czvf $zipFileName2 $1
				numDuplicated2=$(ls ~/TRASH | grep -c "$1.tar.gz")
				#echo $numDuplicated
				# for q8, append the filename if duplicated
				if [ $numDuplicated2 -eq 0 ]
				then
					#out put zipped file
					mv $zipFileName2 ~/TRASH
					echo "[Note]: The Zipped [Directory] is moving to ~/TRASH"
				else
					# output updated dupcated & append date and move
					mv $zipFileName2 $newzipFileName2
					mv $newzipFileName2 ~/TRASH
					echo "[Note]: DATE add to duplicated [Directory], it was moved to ~/TRASH"
				fi
		elif [[ -f $1 ]]; then
		    echo "[Note]: The commandline input $input is a [File]"
				echo "[Note]: The oriiginal [File] $input ----start ziping----"
				gzip -r $1
				numDuplicated=$(ls ~/TRASH | grep -c "$1.gz")
				#echo $numDuplicated
				# for q8, append the filename if duplicated
				if [ $numDuplicated -eq 0 ]
				then
					#out put zipped file
					mv $zipFileName ~/TRASH
					echo "[Note]: The Zipped [File] is moving to ~/TRASH"
				else
					# out put updated dupcated & append date
					mv $zipFileName $newzipFileName
					mv $newzipFileName ~/TRASH
					echo "[Note]: DATE add to duplicated [File], it was moved to ~/TRASH"
				fi
		else
		    echo "[Note]: The commandline input $input is not valid"
		    exit 1
		fi

	else
		# if the file is zipped, move the file
		mv $1 ~/TRASH
	fi

else
	echo "[Error]: the inputfile or directory does not exist in the current directory"
fi
#q9, check the files older than 24 hours and delete
numRemove=$(find ~/TRASH/ -mindepth 1 -mmin +$((1440))| wc -l)
#debug using 1 min
#numRemove=$(find ~/TRASH/ -mindepth 1 -mmin +$((1))| wc -l)

  # 24 hours =24*60= 1440 minutes
	# -mmin +$(number) means find file greater than
	# -mmin -$(number) means find file less than
if [ $numRemove -eq 0 ]
then
	echo "[Note]: No files to delete in TRASH with Condition [ > 24 hours ] "
	else
		find ~/TRASH/ -mindepth 1 -mmin +$((1440)) -delete
		#debug using 1 min
		#find ~/TRASH/ -mindepth 1 -mmin +$((1)) -delete

	echo "[Success]: Successfully safe deleted the file(s)![ Time > 24 hours]"
fi

#echo "[Error]: failed to delete the files"
