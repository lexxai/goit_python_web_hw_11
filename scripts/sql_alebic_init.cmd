@echo off
PUSHD ..\hw11

alembic init migrations

alembic revision --autogenerate -m 'Init'

POPD