class VaccineScheduler(object):
    """
    Common arguments:
        provider_id: Unique provider ID for each provider
        patient_id: Unique patient ID for each patient
        day: Calendar date
        appointment_time: Appointment date and time
    """

    def __init__(self) -> None:
        # self.appointments = {patient_id:{provider_id:"", appt_time:""}}
        # self.provider_appointment = {"date":{provider_id::{appt_times:{8:"",8:30:""}}}
        # self.daily_provider_records = {"date":{{"provider_id":{8:(), 8:30:()}}}}

        self.appointments = {}
        self.provider_appointment = {}
        self.daily_provider_records = {}

    def schedule_appointment(self, patient_id, provider_id, appointment_time):
        """
        Reserve a patient appointment with this provider and appointment time

        Raises:
            Exception: This appointment does not exist or this patient already
                       has an appointment
        """
        day_time_split = appointment_time.split()
        print(day_time_split[0], day_time_split[1])
        try:
            if patient_id not in self.appointments and provider_id in self.provider_appointment[day_time_split[0]]:
                # check provider availability
                if day_time_split[0] in self.provider_appointment:
                    provider_availability = self.provider_appointment[provider_id].get(day_time_split[1], None)
                    if not provider_availability:
                        return False

                self.appointments[patient_id] = {"provider_id": provider_id, "appointment_time": appointment_time[1]}
                self.daily_provider_records[day_time_split[0]] = {provider_id: {day_time_split[1]: [patient_id]}}
                return self.appointments, self.daily_provider_records

        except Exception as e:
            print(f"exception is {e}")
            return False

    def cancel_appointment(self, patient_id):
        """
        Cancel an existing appointment for a patient. If this patient has no
        appointment, do nothing.
        """
        pass

    def get_patient_appointment(self, patient_id):
        """
        Get this patient's appointment information

        Returns:
            A tuple of Provider ID and appointment time with this patient’s
            appointment information, or
            None if this patient has no appointment reserved
        """
        pass

    def get_available_appointments(self, day):
        """
        Get open appointments on this day for patients to browse

        Returns:
            A mapping of appointment time to list of provider IDs indicating
            which providers have available appointments for each appointment
            time on this day
        """
        pass

    def add_appointment(self, provider_id, appointment_time):
        """
        Make a new appointment with this provider available

        Raises:
            Exception: This provider already has an appointment at this time
        """
        #  self.provider_appointment = {"date":{provider_id:{8:"",8:30:""}}}
        day_time_split = appointment_time.split()
        date = day_time_split[0]
        hour = day_time_split[1]
        try:
            if date not in self.provider_appointment:
                self.provider_appointment[date] = {provider_id: {hour: ""}}
            else:
                if date in self.provider_appointment:
                    if provider_id in self.provider_appointment[date]:
                        if hour not in self.provider_appointment[date][provider_id].keys():
                            self.provider_appointment[date][provider_id][hour] = ""
                    else:
                        self.provider_appointment[date][provider_id] = {hour: ""}
        except:
            raise Exception

    def remove_appointment(self, provider_id, appointment_time):
        """
        Remove an available appointment for a provider at this time. If this
        provider has no appointment at this time, do nothing.
        """
        pass

    def get_provider_schedule(self, provider_id, day):
        """
        Get this provider's patient schedule for this day

        Returns:
            A list of tuples containing appointment times and patient IDs,
            sorted by appointment time, which represents the patient schedule
            for this provider on this day
        """
        pass


# check it out later
class VaccineSchedulerC(object):
    def __init__(self):
        # Initialize data structures to keep track of appointments and availability
        self.appointments = {}  # {patient_id: (provider_id, appointment_time)}
        self.availability = {}  # {day: {appointment_time: [provider_ids]}}

    def schedule_appointment(self, patient_id, provider_id, appointment_time):
        if patient_id in self.appointments:
            raise Exception("This patient already has an appointment.")
        if (provider_id, appointment_time) not in self.availability.get(appointment_time, []):
            raise Exception("This appointment does not exist.")
        self.appointments[patient_id] = (provider_id, appointment_time)

    # fix this
    def cancel_appointment(self, patient_id):
        if patient_id in self.appointments:
            _, appointment_time = self.appointments.pop(patient_id)
            self.availability[appointment_time].append(provider_id)

    def get_patient_appointment(self, patient_id):
        if patient_id in self.appointments:
            return self.appointments[patient_id]
        return None

    def get_available_appointments(self, day):
        return self.availability.get(day, {})

    def add_appointment(self, provider_id, appointment_time):
        if (provider_id, appointment_time) in self.availability.get(appointment_time, []):
            raise Exception("This provider already has an appointment at this time.")
        if appointment_time not in self.availability:
            self.availability[appointment_time] = []
        self.availability[appointment_time].append(provider_id)

    def remove_appointment(self, provider_id, appointment_time):
        if appointment_time in self.availability and provider_id in self.availability[appointment_time]:
            self.availability[appointment_time].remove(provider_id)

    def get_provider_schedule(self, provider_id, day):
        schedule = []
        for patient_id, (provider, appointment_time) in self.appointments.items():
            if provider_id == provider and appointment_time.date() == day:
                schedule.append((appointment_time, patient_id))
        return sorted(schedule, key=lambda x: x[0])


ob = VaccineScheduler()
print(ob.add_appointment("345", "08-10-2021 10:30"))
print(ob.schedule_appointment("123", "345", "08-10-2021 10:30"))
