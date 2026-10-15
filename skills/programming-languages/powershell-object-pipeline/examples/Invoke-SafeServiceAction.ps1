#Requires -Version 7.2
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Invoke-SafeServiceAction {
    [CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'Medium')]
    [OutputType([PSCustomObject])]
    param(
        [Parameter(Mandatory = $true, ValueFromPipelineByPropertyName = $true)]
        [ValidatePattern('^[a-zA-Z0-9_-]{1,64}$')]
        [string]$ServiceName,

        [Parameter(Mandatory = $true)]
        [ValidateSet('Start', 'Stop', 'Restart')]
        [string]$Action
    )
    process {
        if ($PSCmdlet.ShouldProcess($ServiceName, $Action)) {
            [PSCustomObject]@{
                Service   = $ServiceName
                Action    = $Action
                Succeeded = $true
            }
        }
    }
}
