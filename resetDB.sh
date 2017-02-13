sqlplus sys/sysdba as sysdba @resetLocalhostDBE.sql
cd /d/Code/pdihub/pe/pe-dbe-common/resources/dbscripts/model
sqlplus dbe/dbe @Full_Create_BD_2_4.sql << __END__
quit
__END__

cd -
