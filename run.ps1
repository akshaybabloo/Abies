# redirect stderr into stdout
$p = &{python -V} 2>&1
# check if an ErrorRecord was returned
$version = if($p -is [System.Management.Automation.ErrorRecord])
{
    # grab the version string from the error message
   Write-Output $p.Exception.Message
}
else 
{
    # otherwise return as is
   Write-Output $p
}