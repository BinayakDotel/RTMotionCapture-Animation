using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using UnityEngine;
using Firebase.Database;
using Firebase.Extensions;

public class FirebaseAccess : MonoBehaviour
{
    private static DatabaseReference databaseReference;

    private static bool _connection;
    private static bool _refresh = true;

    //public List<string> keypoints = new List<string>();
    private List<KeyPoint> keypoints = new List<KeyPoint>(); 

    public static FirebaseAccess _instance;
    public static FirebaseAccess Instance
    {
        get { return _instance; }
    }

    private void Awake()
    {
        if (_instance != null && _instance != this)
        {
            Destroy(this.gameObject);
            return;
        }

        _instance = this;
        DontDestroyOnLoad(this.gameObject);
    }
    public void Start()
    {
        databaseReference = FirebaseDatabase.DefaultInstance.RootReference;
    }
    public void Update()
    {
        CheckInternet();

        if (_connection && _refresh)
        {
            FirebaseDatabase.DefaultInstance.GetReference("KEYPOINTS").ValueChanged += FirebaseAccess_ValueChanged;
            _refresh = false;
        }
    }
    private void FirebaseAccess_ValueChanged(object sender, ValueChangedEventArgs e)
    {
        foreach(var key in e.Snapshot.Children)
        {
            KeyPoint keypoint = new KeyPoint(key.Key);
            foreach(var value in key.Children)
            {
                try
                {
                    keypoint.SetCoordinate(value.Key, float.Parse(value.Value.ToString()));
                }
                catch
                {
                    print("SOMETHING WRONG!");
                }
            }
            keypoints.Add(keypoint);
            keypoint = null;
        }
        Animate.Instance.MovePart(keypoints);
    }

    public void CheckInternet()
    {
        if (Application.internetReachability == NetworkReachability.NotReachable)
        {
            _connection = false;
            _refresh = true;
            return;
        }
        _connection = true;
    }
}
