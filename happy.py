import random
from gtts import gTTS
import os

def ppl_determination():
  exc = {"Neck Rotation":"Take a deep breath in, and exhale while turning the head to one side, looking over that shoulder. Hold. Repeat on the opposite side.", "Neck Lateral Flexion":"Take a deep breath in. Exhale as the neck bends to one side and the ear goes down towards the shoulder. Hold. Repeat on the opposite side.", ". Neck Forward Flexion":"Take a deep breath in. Exhale as you slowly lower the chin to the chest. Hold.", "Shoulder Rolls with Depression":"Take a deep breath in, and roll the shoulders up towards the ears. Exhale and roll the shoulders back while depressing. Hold.", "Posterior Deltoid Stretch":"Take a deep breath in, and extend one arm out in front of you. Exhale as you hook the arm slightly above the elbow with the opposite hand, bringing it across and in towards the chest.", "Tricep Stretch": "Take a deep breath in, and extend both arms above the head. Reach down the center of the back with one arm, and exhale, pressing down slightly with the opposite hand on the elbow. Repeat on theopposite side.", "Trunk Rotation": "Place the hand on the opposite thigh. Take a deep breath in and exhale while twisting the torso, looking over the shoulder. Hold,and repeat on the opposite side.", "Lateral Trunk Flexion": "With the arms at your side, take a deep breath in, and exhale as the trunk bends to the left and the right arm extends overhead. Hold, and repeat on the opposite side.", "Rhomboid Stretch": "Extend the arms out in front, crossing them over so the palms are touching. Inhale and raise the arms up to shoulder height. Exhale and push the shoulders forward. Hold."}
  ex=list(exc.keys())
  exc12=len(exc.keys())
  exc1 = random.randrange(0,exc12)
  exc3 = (ex[exc1]+"\n"+ exc[ex[exc1]])
  return exc3

data=ppl_determination()
language = 'en'
myobj = gTTS(text=data, lang=language, slow=False)
myobj.save("welcome.mp3")

def ppl_exercise():
  
  ria={"Chest Stretch":"In a seated or standing position, take the arms behind you and, if you can, lace your fingers together. Straighten the arms and gently lift your hands up a few inches until you feel a stretch in your chest. Hold for 10 to 30 seconds. Avoid this move if you have shoulder problems.", "Shoulder Shrug":"Seated or standing, lift the shoulders up towards the ears, squeezing them as hard as you can. Hold for 1 to 2 seconds and roll them back as you relax down. Repeat for 8 to 10 reps and then roll the shoulders forward.", "Upper Back Stretch": "Seated or standing, stretch the arms straight out and rotate the hands so that the palms face away from each other. Cross the arms so that the palms are pressed together, contract the abs and round the back, reaching away as you relax the head. Don't collapse but, instead, imagine you're curving up and over an imaginary ball. Hold the stretch for 10 to 30 seconds. If twisting the arms doesn't feel good, simply lace the fingers together.", "Spinal Twist": "In a seated position with the feet flat on the floor, contract the abs and gently rotate the torso towards the right. Use your hands on the armrest or seat of the chair to help deepen the stretch. Only twist as far as you comfortably can and keep the back straight while keeping the hips square. Hold for 10 to 30 seconds and repeat on the other side.", "Torso Stretch":"Seated or standing, lace the fingers together and stretch them up towards the ceiling. Take a deep breath as you stretch up as high as you can, then exhale and open the arms, sweeping them back down. Repeat for 8 to 10 reps.","Forearm Stretch":"Seated or standing, stretch the right arm out and turn the hand down so that the fingers point towards the floor. Use the left hand to gently pull the fingers towards you, feeling a stretch in the forearm. Hold for 10 to 30 seconds and repeat on the other hand.", "Neck Stretch":"Sitting in your chair, reach down and grab the side of the chair with the right hand and gently pull while tilting your head to the left, feeling a stretch down the right side of the neck and shoulder. Hold for 10 to 30 seconds and repeat on the other side.", "Hip Flexor Stretch":"While standing, take the right leg back a few feet. Bend the back knee, almost like you're doing a lunge, and lower both knees until you feel a stretch in the front of the right hip. Squeeze the glutes of the back leg to deepen the stretch. Hold for 10 to 30 seconds and repeat on the other side.", "Seated Hip Stretch": "While seated, cross the right ankle over the left knee and sit up nice and tall. Gently lean forward, keeping the back straight and reaching out with the torso until you feel a stretch in the right glute and hip. You can also press down on the right knee to deepen the stretch. Hold for 10 to 30 seconds and repeat on the other side. Skip this move if it bothers the knees."}

  shre=list(ria.keys())
  yas=len(ria.keys())
  nan = random.randrange(0,yas)
  return (shre[nan]+"\n"+ria[shre[nan]])


data1=ppl_exercise()
language = 'en'
myobj = gTTS(text=data1, lang=language, slow=False)
myobj.save("welcome1.mp3")