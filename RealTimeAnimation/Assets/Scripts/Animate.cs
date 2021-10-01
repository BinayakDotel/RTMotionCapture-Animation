using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*public class Animate : MonoBehaviour
{
    [Header("Spine")]
    public GameObject Spine;
    public Vector3 SpinePosEndPoint;
    public Vector3 SpineRotEndPoint;

    [Header("UpperRightLeg")]
    public GameObject UpperRightLeg;
    public Vector3 UpperRightLegPosEndPoint;
    public Vector3 UpperRightLegRotEndPoint;

    public GameObject Right_Ankle;
    public GameObject Left_Ankle;

    public float Right_Angle;
    public float Left_Angle;

    [Header("UpperLeftLeg")]
    public GameObject UpperLeftLeg;
    public Vector3 UpperLeftLegPosEndPoint;
    public Vector3 UpperLeftLegRotEndPoint;

    [Header("Speed")]
    public float smooth_move;
    public float smooth_rot;

    [Header("DATA")]
    public Vector2 LatLon;

    public static Animate _instance;
    public static Animate Instance
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
        UpperRightLegPosEndPoint = UpperRightLeg.transform.position;
        UpperLeftLegPosEndPoint = UpperLeftLeg.transform.position;

        smooth_move = 2f;
        smooth_rot = 40;
        SpinePosEndPoint = Spine.transform.position;
        SpineRotEndPoint = new Vector3(0f,-90f,-90f);

        UpperRightLegRotEndPoint = new Vector3(0f, -90f, 90f);
        UpperLeftLegRotEndPoint = new Vector3(0f, -90f, -90f);

    }
    public void Update()
    {*/
        /*Spine.transform.position = Vector3.Lerp(Spine.transform.position, 
            SpinePosEndPoint, smooth_move * Time.deltaTime);
        
        Quaternion currentRotationOfSpine = Spine.transform.rotation;
        Quaternion wantedRotationOfSpine = Quaternion.Euler(SpineRotEndPoint);
        Spine.transform.rotation = Quaternion.RotateTowards(currentRotationOfSpine,
            wantedRotationOfSpine, Time.deltaTime * smooth_rot);

        UpperRightLeg.transform.position = Vector3.Lerp(UpperRightLeg.transform.position,
            UpperRightLegPosEndPoint, smooth_move * Time.deltaTime);

        Quaternion currentRotationOfUpperRightLeg = UpperRightLeg.transform.rotation;
        Quaternion wantedRotationOfUpperRightLeg = Quaternion.Euler(UpperRightLegRotEndPoint);
        UpperRightLeg.transform.rotation = Quaternion.RotateTowards(currentRotationOfUpperRightLeg,
            wantedRotationOfUpperRightLeg, Time.deltaTime * smooth_rot);

        UpperLeftLeg.transform.position = Vector3.Lerp(UpperLeftLeg.transform.position,
            UpperLeftLegPosEndPoint, smooth_move * Time.deltaTime);

        Quaternion currentRotationOfUpperLeftLeg = UpperLeftLeg.transform.rotation;
        Quaternion wantedRotationOfUpperLeftLeg = Quaternion.Euler(UpperLeftLegRotEndPoint);
        UpperLeftLeg.transform.rotation = Quaternion.RotateTowards(currentRotationOfUpperLeftLeg,
            wantedRotationOfUpperLeftLeg, Time.deltaTime * smooth_rot);*/

        /*Quaternion currentRotationOfUpperRightLeg = UpperRightLeg.transform.rotation;
        Quaternion wantedRotationOfUpperRightLeg = Quaternion.Euler(UpperRightLegRotEndPoint);
        UpperRightLeg.transform.rotation = Quaternion.RotateTowards(currentRotationOfUpperRightLeg,
            wantedRotationOfUpperRightLeg, Time.deltaTime * smooth_rot);

        Quaternion currentRotationOfUpperLeftLeg = UpperLeftLeg.transform.rotation;
        Quaternion wantedRotationOfUpperLeftLeg = Quaternion.Euler(UpperLeftLegRotEndPoint);
        UpperLeftLeg.transform.rotation = Quaternion.RotateTowards(currentRotationOfUpperLeftLeg,
            wantedRotationOfUpperLeftLeg, Time.deltaTime * smooth_rot);

    }
    public void MovePart(List<KeyPoint> keyPoints) {
        foreach(KeyPoint keyPoint in keyPoints)
        {
            //print($"MOVING::{keyPoint.getName()}-->{keyPoint.getCoordinate()}");
            DetermineAngle(keyPoint.getName(), keyPoint.getCoordinate());
        }
    }
    public void DetermineAngle(string name, Vector3 newPos)
    {
        if (name == "RIGHT_ANKLE")
        {
            UpperRightLegRotEndPoint.x = Mathf.Atan((newPos.x - Right_Ankle.transform.position.x) / (newPos.y - Right_Ankle.transform.position.y)) * 180 / Mathf.PI;
            print($"{name}-->{UpperRightLegRotEndPoint.x}");
        }
        if (name == "LEFT_ANKLE")
        { 
            UpperLeftLegRotEndPoint.x = Mathf.Atan((newPos.x - Left_Ankle.transform.position.x) / (newPos.y - Left_Ankle.transform.position.y)) * 180 / Mathf.PI;
            print($"{name}-->{UpperLeftLegRotEndPoint.x}");
        }
    }
}
*/