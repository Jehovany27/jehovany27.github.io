// script.js
// Configuration Firebase
const firebaseConfig = {
  apiKey: "VOTRE_API_KEY",
  authDomain: "votre-projet.firebaseapp.com",
  databaseURL: "https://votre-projet.firebaseio.com",
  projectId: "votre-projet",
  storageBucket: "votre-projet.appspot.com",
  messagingSenderId: "ID_DE_VOTRE_SENDER",
  appId: "VOTRE_APP_ID"
};

// Initialisation Firebase
firebase.initializeApp(firebaseConfig);
const db = firebase.database();
const knowledgeRef = db.ref('connaissances');

// Soumission du formulaire
document.getElementById('knowledgeForm').addEventListener('submit', (e) => {
  e.preventDefault();
  const knowledgeInput = document.getElementById('knowledgeInput').value;
  if (knowledgeInput.trim() !== '') {
    knowledgeRef.push({ text: knowledgeInput.trim() });
    document.getElementById('knowledgeInput').value = '';
  }
});

// Affichage des connaissances partagées en temps réel
knowledgeRef.on('child_added', (snapshot) => {
  const knowledge = snapshot.val();
  const li = document.createElement('li');
  li.className = 'list-group-item';
  li.textContent = knowledge.text;
  document.getElementById('knowledgeList').appendChild(li);
});
