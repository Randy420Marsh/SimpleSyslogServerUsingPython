If the application does not work, the port may already be in use.
If it does not work change the port e.q. 555 or alternatively kill the existing program.
To kill the existing app use these commands in admim cmd prompt.

win+r > type cmd and press ctrl+shift+enter


------------------------------------------------------------------

To find the pid of the running program for the port

netstat -ano | findstr :514

------------------------------------------------------------------

This will kill the existing program using the port

taskkill /PID <PID_NUMBER> /F

------------------------------------------------------------------