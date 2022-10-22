@echo off
setlocal

:__LAUNCH__
echo Launch...
docker-compose build
start http://localhost:8888
docker-compose up
goto __END__

:__END__
