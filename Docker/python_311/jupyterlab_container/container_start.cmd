@echo off
setlocal

:__LAUNCH__
echo Launch...
docker-compose build
start http://localhost:9000
docker-compose up
goto __END__

:__END__
