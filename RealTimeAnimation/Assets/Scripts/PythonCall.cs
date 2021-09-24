using System.Collections;
using System.Collections.Generic;
using IronPython.Hosting;
using UnityEngine;

public class PythonCall : MonoBehaviour
{
    // Use this for initialization
    void Start()
    {
        var engine = Python.CreateEngine();

        ICollection<string> searchPaths = engine.GetSearchPaths();

        //Path to the folder of greeter.py
        searchPaths.Add(Application.dataPath);
        //Path to the Python standard library
        searchPaths.Add(Application.dataPath + @"\Plugins\Lib\");
        engine.SetSearchPaths(searchPaths);

        dynamic py = engine.ExecuteFile(Application.dataPath + @"\greeter.py");
        dynamic greeter = py.Greeter("Binayak");
        print($"{greeter.greet()}");
    }
}
