import { useEffect, useState } from "react";

function LogTable({ activities: initialActivities }) {
  const [activities, setActivities] = useState(initialActivities || []);
  const [loading, setLoading] = useState(!initialActivities);

  useEffect(() => {
    // Dacă nu primesc props cu activities, fac fetch
    if (!initialActivities) {
      setLoading(true);
      fetch("http://localhost:8000/log") // adaptează URL-ul după nevoie
        .then((res) => res.json())
        .then((data) => {
          setActivities(data);
          setLoading(false);
        })
        .catch((err) => {
          console.error("Eroare la fetch activități:", err);
          setLoading(false);
        });
    }
  }, [initialActivities]);

  if (loading) return <p className="text-sm text-gray-500">Se încarcă activitățile...</p>;

  if (!activities || activities.length === 0)
    return <p className="text-sm text-gray-500">Nicio activitate sincronizată momentan.</p>;

  return (
    <div className="overflow-x-auto mt-4 border rounded shadow">
      <table className="min-w-full text-sm text-left border-collapse border">
        <thead className="bg-gray-100 text-xs uppercase">
          <tr>
            <th className="border px-3 py-2">Activity ID</th>
            <th className="border px-3 py-2">Nume</th>
            <th className="border px-3 py-2">UWI</th>
            <th className="border px-3 py-2">Start</th>
            <th className="border px-3 py-2">Finish</th>
            <th className="border px-3 py-2">Status</th>
            <th className="border px-3 py-2">Cod RigView</th>
          </tr>
        </thead>
        <tbody>
          {activities.map((a, i) => (
            <tr key={a.activity_id || i} className="border-t hover:bg-zinc-50">
              <td className="border px-3 py-1">{a.activity_id}</td>
              <td className="border px-3 py-1">{a.name}</td>
              <td className="border px-3 py-1">{a.uwi}</td>
              <td className="border px-3 py-1">
                {a.start ? new Date(a.start).toLocaleString() : "-"}
              </td>
              <td className="border px-3 py-1">
                {a.finish ? new Date(a.finish).toLocaleString() : "-"}
              </td>
              <td className="border px-3 py-1">{a.status}</td>
              <td className="border px-3 py-1">{a.rig_view_code}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default LogTable;
