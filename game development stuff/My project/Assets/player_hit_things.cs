using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class player_hit_things : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    
    void OnCollisionEnter(Collision collisionObject)
    {
        if (Equals(collisionObject<Collider>().tag, "wall"))
        {
            //we hit a wall... what should happen?
            //player takes damage
            // Restart the level.
        }
    }
}
