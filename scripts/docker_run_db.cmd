@echo off

docker run --name pg-hw11 -p 5432:5432 --env-file ../.env -d postgres


                    

