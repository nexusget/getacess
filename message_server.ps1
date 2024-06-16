# message_server.ps1

$listener = [System.Net.HttpListener]::new()
$listener.Prefixes.Add("http://*:8080/")
$listener.Start()
Write-Output "Listening for messages on port 8080..."

while ($true) {
    $context = $listener.GetContext()
    $request = $context.Request
    $response = $context.Response
    $body = (New-Object IO.StreamReader $request.InputStream).ReadToEnd()
    
    Add-Type -AssemblyName PresentationFramework
    [System.Windows.MessageBox]::Show($body, "Message from [Hacker{surprise}]")
    
    $response.StatusCode = 200
    $response.Close()
}
