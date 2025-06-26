import { useState } from "react";

export default function SyncButton() {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState(null);
  const [activities, setActivities] = useState([]);

  const handleSync = async () => {
    setLoading(true);
    setMessage(null);

    try {
      const response = await fetch("http://localhost:8000/sync/activities");
      if (!response.ok) {
        throw new Error("Eroare la sincronizare");
      }

      const data = await response.json();
      setActivities(data);
      setMessage(`✅ ${data.length} activități sincronizate`);
    } catch (err) {
      setMessage(`❌ ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center space-y-4">
      <button
        onClick={handleSync}
        disabled={loading}
        className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
      >
        {loading ? "Sincronizează..." : "Sincronizează activitățile"}
      </button>

      {message && <p className="text-sm text-gray-700">{message}</p>}

      {activities.length > 0 && (
        <div className="mt-4 w-full max-w-2xl text-left text-sm">
          <h3 className="font-semibold mb-2">Activități sincronizate:</h3>
          <ul className="bg-white border rounded p-4 max-h-60 overflow-y-auto shadow">
            {activities.map((a, index) => (
              <li key={index} className="mb-1">
                <span className="font-medium">{a.name}</span> – {a.uwi} ({a.rig_view_code})
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
