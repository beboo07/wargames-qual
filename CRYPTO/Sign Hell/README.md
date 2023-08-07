this chall i did it in a python shell so i will just drop soem screenshots 

first getting the vars from the server 



then using this web or the discrete_log function in python to calculate a from g a p we got 
https://github.com/beboo07/wargames-qual/blob/main/CRYPTO/Sign%20Hell/image%20(1).png?raw=true
![image](https://github.com/beboo07/wargames-qual/blob/main/CRYPTO/Sign%20Hell/image%20(1).png)

 Find exp such that 11exp ≡ 34 134298 725371 964782 007764 476293 175780 055142 033662 685897 632429 885462 742925 280365 387011 692649 796046 732529 629544 466504 901330 080949 485478 616291 453730 871519 975397 826191 307378 (170 digits) (mod 164 437942 065266 857969 581628 824832 401887 621370 656671 776137 458558 111452 951927 383282 534829 190858 022885 766391 991997 353384 332740 973841 301613 047525 042932 844119 097061 295817 984001 (171 digits))

exp = 108088 186520 659225 400742 357877 518081 338396 444861 965202 522576 980361 916243 958733 (78 digits) + 164 437942 065266 857969 581628 824832 401887 621370 656671 776137 458558 111452 951927 383282 534829 190858 022885 766391 991997 353384 332740 973841 301613 047525 042932 844119 097061 295817 984000 (171 digits)k


and last i got the flag with the inverse of s2 
Note the GCD(s2,p-1)!=0 so u need to calc the mod_inverse (s2//GCD(s1,p-1),p-1) then divide the result after multiple it with s1 inverse with s2 
![image](https://github.com/beboo07/wargames-qual/blob/main/CRYPTO/Sign%20Hell/image%20(2).png)
