this chall i did it in a python shell so i will just drop soem screenshots 

first getting the vars from the server 

![image](https://github.com/beboo07/wargames-qual/blob/main/CRYPTO/Sign%20Hell/image.png)


then using this web or the discrete_log function in python to calculate a from g a p we got 
(https://www.alpertron.com.ar/DILOG.HTM)
![image](https://github.com/beboo07/wargames-qual/blob/main/CRYPTO/Sign%20Hell/image4.png)


and last i got the flag with the inverse of s2 
Note the GCD(s2,p-1)!=0 so u need to calc the mod_inverse (s2//GCD(s1,p-1),p-1) then divide the result after multiple it with s1 inverse with s2 
![image](https://github.com/beboo07/wargames-qual/blob/main/CRYPTO/Sign%20Hell/image%20(1).png)
![image](https://github.com/beboo07/wargames-qual/blob/main/CRYPTO/Sign%20Hell/image%20(2).png)
