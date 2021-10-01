using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Diagnostics;

public class LaunchPython : MonoBehaviour
{
	[SerializeField] Server lp;
	[SerializeField] string path, run_python, power_shell;

	private void Awake()
	{
		lp = GameObject.Find("AnimationServer").GetComponent<Server>();
		path = System.IO.Directory.GetCurrentDirectory() + "/Assets/Python/PythonScripts/Test.py";

		run_python = System.IO.Directory.GetCurrentDirectory() + @"\Assets\Scripts\PythonScripts\Estimator.py";
		power_shell = @"powershell.exe";
	}
	public void CallPython()
	{
		print($"PATH::{path}");
        //StartCoroutine(Execute());
        RunCmd();
	}
	IEnumerator Execute()
	{
		print("RUN THREAD");
		yield return new WaitForSeconds(0);

        Process process = Process.Start("powershell.exe", "-NoExit -Command /python Estimator.py");
        process.WaitForExit();
        process.Close();
	}
    public void RunCmd()
    {
        var psi = new ProcessStartInfo();
        psi.FileName = @"C:\Users\User\AppData\Local\Programs\Python\Python39\python.exe";

        var script = run_python;

        psi.UseShellExecute = false;
        psi.CreateNoWindow = false;
        psi.RedirectStandardOutput = true;
        psi.RedirectStandardError = true;

        var errors = "";
        var results = "";

        using(var process = Process.Start(psi))
		{
            errors = process.StandardError.ReadToEnd();
            results = process.StandardOutput.ReadToEnd();
		}

        print($"Errors::{errors}");
        print($"Results::{results}");
    }
    IEnumerator Run()
    {
        yield return new WaitForSeconds(0);

        // start the child process
        Process process = new Process();

        // redirect the output stream of the child process.
        process.StartInfo.UseShellExecute = false;
        process.StartInfo.RedirectStandardOutput = true;
        process.StartInfo.CreateNoWindow = true;
        process.StartInfo.FileName = "cmd.bat";

        
        process.StartInfo.WorkingDirectory = Application.temporaryCachePath; // nb. can only be called on the main thread

        int exitCode = -1;
        string output = null;

        try
        {
            process.Start();

            // do not wait for the child process to exit before
            // reading to the end of its redirected stream.
            // process.WaitForExit();

            // read the output stream first and then wait.
            output = process.StandardOutput.ReadToEnd();
            process.WaitForExit();
        }
        catch (System.Exception e)
        {
            print("Run error" + e.ToString()); // or throw new Exception
        }
        finally
        {
            exitCode = process.ExitCode;

            process.Dispose();
            process = null;
        }

        // process exitCode/output, call onComplete handlers etc.
        // ...
    }
}
