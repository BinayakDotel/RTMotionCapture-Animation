using UnityEngine;

public class KeyPoint
{
    private string name;
    private float x, y, z;

    public KeyPoint(string name)
    {
        this.name = name;
    }

    public void SetCoordinate(string axis, float point)
    {
        if (axis.Equals("x")) this.x = point;
        if (axis.Equals("y")) this.y = point;
        if (axis.Equals("z")) this.z = point;
    }

    public string getName()
    {
        return this.name;
    }
    public Vector3 getCoordinate()
    {
        return new Vector3(this.x, this.y, this.z);
    }
}
